package main

// *****************************************************
// *****************************************************
// Please do not change anything in this file.
// You may change the number at the bottom (1000000 to 10)
// for testing purposes. Your code will be run against
// the 1000000, however.
// *****************************************************
// *****************************************************

import (
	crand "crypto/rand"
	"encoding/hex"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"sync"
	"time"
)

// Road is a road object that contains a name and a road to the right, left, and straight of the road. These roads could, in theory, intersect.
// However, for simplicity's sake we won't make any of the roads repeated.
type Road struct {
	name     string
	left     *Road
	right    *Road
	straight *Road
}

// The city contains an entrance to the first road item. The city can be thought of like a trinary tree (3 branch version of a binary tree) without a guarantee that
// there will be completeness among the leaf nodes (road objects)
type City struct {
	entrance *Road
}

// RandName is a simple random naming function. the name is not used in this code but it's nice to have
func RandName() string {
	bytes := make([]byte, 4)
	crand.Read(bytes)
	return hex.EncodeToString(bytes)
}

/*
From here forward is code to test the function you will be debugging. You're more than welcome to look through it for clues about how to construct the city.
If you want to do some quicker debugging feel free to change the numRoads value at the bottom of the page to something more reasonable. However, be aware that your function will be run multiple times against
larger numbers for testing.
*/

func exploreRoad(r *Road, c chan struct{}, wg *sync.WaitGroup) {
	defer wg.Done()
	if r != nil {
		c <- struct{}{}
		wg.Add(3)
		go exploreRoad(r.left, c, wg)
		go exploreRoad(r.right, c, wg)
		go exploreRoad(r.straight, c, wg)
	}
}

func (city *City) verifyRoads(numRoads int) {
	wg := sync.WaitGroup{}
	c := make(chan struct{}, numRoads)
	wg.Add(1)
	go exploreRoad(city.entrance, c, &wg)
	wg.Wait()
	close(c)
	roadsFound := 0
	for range c {
		roadsFound++
	}
	fmt.Println("Number of Roads Found : " + strconv.Itoa(roadsFound))
	if roadsFound == numRoads {
		fmt.Println("Success! Great Job!!")
		return
	}
	fmt.Println("Try again!")
}

func timer() {
	<-time.After(30 * time.Second)
	fmt.Println("30 second timeout reached.")
	os.Exit(1)
}

func main() {
	start := time.Now()
	rand.Seed(start.Unix())
	go timer()
	numRoads := (rand.Int() % 1000000) + 1000000
	city := makeRandomCity(numRoads)
	city.verifyRoads(numRoads)
	fmt.Printf("Time taken : %s\n", time.Since(start))
}
