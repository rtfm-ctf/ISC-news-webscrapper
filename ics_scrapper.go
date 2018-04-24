package main

import (
	"fmt"
	"os"

	"github.com/anaskhan96/soup"
)

func main() {
	response, err := soup.Get("https://isc.sans.edu/podcast.html")
	if err != nil {
		fmt.Printf("Stderr: %s", err)
		os.Exit(1)
	}
	parsed := soup.HTMLParse(response)
	news := parsed.Find("blockquote").FindAll("a")
	for _, news := range news {
		fmt.Println(news.Text())
	}
}
