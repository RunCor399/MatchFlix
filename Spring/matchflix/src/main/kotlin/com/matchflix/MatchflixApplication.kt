package com.matchflix

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class MatchflixApplication

fun main(args: Array<String>) {
	runApplication<MatchflixApplication>(*args)
}
