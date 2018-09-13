package main

// *****************************************************
// *****************************************************
// Feel free to change anything in this file
// *****************************************************
// *****************************************************

import (
	"fmt"
	"strconv"
	"sync"
)

// MakeRoad is where the meat and potatoes of the work you will be doing will get done. It is intended to take reference to and instantiate a road, it does this
// by checking the channel to see if we've generated a city of a large enough size yet (i.e. the channel is empty). If we have a large enough city then return.
// Otherwise, we need to continue to make more roads and we do so by whatever means you devise to be optimal.
// Hints:
// - A linter might help, but there are some syntax erros here as well
// - Road instantiation doesn't appear to be working. What could be the reason for that?
func (r *Road) MakeRoad(c chan int, wg *sync.WaitGroup) {
	// fmt.Println("In MakeRoad")
	// release from the waitgroup later
	defer wg.Done()
	// if we can pull of the channel we have more roads to generate
	select {
	case _, ok := <- c:
			if ok == false {
				return
			}
		default:
			return
	}

	// we create the new road
	//r = new(Road)
	r = &Road{name: RandName()}
	fmt.Println(*r)
	// and move forward, further into the city
	wg.Add(3)
	go r.left.MakeRoad(c, wg)
	go r.right.MakeRoad(c, wg)
	go r.straight.MakeRoad(c, wg)

}

// makeRandomCity operates sort of like the wrapper function to MakeRoad. We make the entry point, populate the channel for road creation tracking, and unleash the MakeRoad function
// you will need to change this function as well in order to get the city construction working.
func makeRandomCity(numRoads int) (city *City) {
	fmt.Println("Number of roads in automatically generated city : " + strconv.Itoa(numRoads))
	// create a channel with the size of numRoads (and population of numRoads) for tracking purposes
	c := make(chan int, numRoads)
	for i := 0; i < numRoads; i++ {
		// fmt.Println(strconv.Itoa(i))
		c <- i
	}
	close(c)
	// we create the entrypoint into the city
	r := &Road{name: "entry"}
	r.left = &Road{name: RandName()}
	// create the waitgroup so we don't have any timing issues
	wg := sync.WaitGroup{}
	// unleash makeroad
	wg.Add(3)
	go r.left.MakeRoad(c, &wg)
	go r.right.MakeRoad(c, &wg)
	go r.straight.MakeRoad(c, &wg)
	// wait for it
	wg.Wait()
	// and set the named return value
	city = &City{r}
	return city
}
