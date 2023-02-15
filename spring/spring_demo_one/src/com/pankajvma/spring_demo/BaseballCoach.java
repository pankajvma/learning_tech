package com.pankajvma.spring_demo;

public class BaseballCoach implements Coach {
	
	// define a private field for the dependency
	private FortuneService fortuneService;
	
	// define a constructor for dependency injection
	public BaseballCoach(FortuneService theFortuneService) {
		fortuneService = theFortuneService;
	}
	
	@Override
	public String getDailyWorkout() {
		return "Spend 30 minutes in Batting practice.";
	}

	@Override
	public String getDailyFortune() {
		// use fortuneService to get the fortune
		return fortuneService.getFortune();
	}
}
