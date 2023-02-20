package com.pankajvma.springdemo;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class PropertyJavaConfigDemoApp {

	public static void main(String[] args) {
		// load and read spring config class
		AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SportConfig.class);
		
		// get the bean from spring container
		SwimCoach theCoach = context.getBean("swimCoach", SwimCoach.class);
		
		// call the method on the bean
		System.out.println(theCoach.getDailyWorkout());
		
		// call method to get daily fortune
		System.out.println(theCoach.getDailyFortune());
		
		// get instance variable values from bean
		System.out.println("team: " + theCoach.getTeam());
		System.out.println("email: " + theCoach.getEmail());
		
		// close the context
		context.close();
	}

}