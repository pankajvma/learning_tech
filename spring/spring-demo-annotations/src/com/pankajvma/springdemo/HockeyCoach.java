package com.pankajvma.springdemo;

import org.springframework.stereotype.Component;

// Practice activity #4

@Component	// Spring will automatically register this beans with the spring container, and we will use the default bean id of "hockeyCoach". "hockeyCoach" can later be used to retrieve that bean from the container. 
public class HockeyCoach implements Coach {

	@Override
	public String getDailyWorkout() {

		return "Practice your sprints";
	}

	@Override
	public String getDailyFortune() {
		// TODO Auto-generated method stub
		return null;
	}

}
