package com.pankajvma.springdemo;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class SwimCoach implements Coach {
	
	@Value("${foo.team}")
	private String team;
	
	@Value("${foo.email}")
	private String email;
	
	private FortuneService fortuneService;
	
	public SwimCoach(FortuneService fortuneService) {

		this.fortuneService = fortuneService;
	}

	@Override
	public String getDailyWorkout() {

		return "Swim swim swim!!!";
	}

	@Override
	public String getDailyFortune() {

		return fortuneService.getFortune();
	}

	public String getTeam() {
		return team;
	}

	public String getEmail() {
		return email;
	}

}
