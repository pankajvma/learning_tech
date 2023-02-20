package com.pankajvma.springdemo;

import org.springframework.stereotype.Component;

@Component
public class KhoKhoCoach implements Coach {

	private FortuneService fortuneService;
	
	public KhoKhoCoach(FortuneService fortuneService) {

		this.fortuneService = fortuneService;
	}
	
	@Override
	public String getDailyWorkout() {
		// TODO Auto-generated method stub
		return "Run 50 short sprints of 10 meters";
	}

	@Override
	public String getDailyFortune() {
		// TODO Auto-generated method stub
		return fortuneService.getFortune();
	}

}
