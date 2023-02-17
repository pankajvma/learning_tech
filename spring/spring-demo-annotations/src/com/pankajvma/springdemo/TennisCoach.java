package com.pankajvma.springdemo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component("thatSillyCoach")	// Spring will automatically register this beans with the spring container, and we will use the bean id of "thatSillyCoach". "thatSillyCoach" can later be used to retrieve that bean from the container. 
public class TennisCoach implements Coach {
	
	@Autowired			// Field injection with @Autowired, We don't need any setters!
	@Qualifier("randomFortuneService") // Since we have multiple implementations of the Fortune service, We have to specify the bean ID of the implementation we would like to use.
	private FortuneService fortuneService;
	
	/*
	@Autowired  // constructor injection using autowired annotation
	public TennisCoach(FortuneService theFortuneService) {
		this.fortuneService = theFortuneService;
	}*/
	
	/*
	@Autowired 	// setter injection using autowired annotation
	public void setFortuneService(FortuneService fortuneService) {
		System.out.println(">> inside setFortuneService() setter method");
		this.fortuneService = fortuneService;
	}*/
	
	public TennisCoach() {
		System.out.println(">> inside tennis coach default constructor.");
	}

	@Override
	public String getDailyWorkout() {

		return "Practice your backhand volley";
	}

	@Override
	public String getDailyFortune() {

		return fortuneService.getFortune();
	}

}
