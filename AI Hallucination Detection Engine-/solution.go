package main

import (
	"fmt"
	"sort"
)

type Response struct {
	ID         int
	Time       int
	Confidence int
	FactCheck  int
}

func main() {

	responses := []Response{
		{101, 1, 90, 30},
		{102, 3, 95, 20},
		{103, 15, 60, 90},
		{104, 18, 92, 40},
	}

	sort.Slice(responses, func(i, j int) bool {
		return responses[i].Time < responses[j].Time
	})

	incidents := 0
	lastHallucinationTime := -100

	for _, r := range responses {

		if r.Confidence > 80 && r.FactCheck < 50 {

			fmt.Printf("Response %d -> HALLUCINATION\n", r.ID)

			if r.Time-lastHallucinationTime > 10 {
				incidents++
			}

			lastHallucinationTime = r.Time

		} else {
			fmt.Printf("Response %d -> SAFE\n", r.ID)
		}
	}

	fmt.Println("Incidents =", incidents)
}
