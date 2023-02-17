package com.pankajvma.springdemo;
import org.springframework.stereotype.Component;

@Component
public class RESTFortuneService implements FortuneService {

	@Override
	public String getFortune() {

		return "Nice, you have connected to the REST API";
	}

}