package com.pankajvma.spring_demo;

public class CricketCoach implements Coach {
	
	// define a private field for the dependency
	private FortuneService fortuneService;
	
	// define literal values
	private String emailAddress;
	private String team;
	
	// our no-args constructor
	public CricketCoach() {
		System.out.println("CricketCoach: inside no-args contructor");
	}
	
	// our setter method
	public void setFortuneService(FortuneService fortuneService) {
		System.out.println("CricketCoach: inside setter method - setFortuneService");
		this.fortuneService = fortuneService;
	}

	public void setEmailAddress(String emailAddress) {
		this.emailAddress = emailAddress;
		System.out.println("CricketCoach: inside setter method - setEmailAddress");
	}

	public void setTeam(String team) {
		this.team = team;
		System.out.println("CricketCoach: inside setter method - setTeam");
	}

	public String getEmailAddress() {
		return emailAddress;
	}

	public String getTeam() {
		return team;
	}

	@Override
	public String getDailyWorkout() {

		return "Practice taking 4 runs by running on pitch";
	}

	@Override
	public String getDailyFortune() {
		// TODO Auto-generated method stub
		return fortuneService.getFortune();
	}

}
