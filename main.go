package main

import (
	"fmt"

	"github.com/BurntSushi/toml"
)

type config struct {
	Message string `toml:"message"`
}

func main() {
	message := "Hello, World!"

	var cfg config
	if _, err := toml.DecodeFile("config.toml", &cfg); err == nil && cfg.Message != "" {
		message = cfg.Message
	}

	fmt.Println(message)
}
