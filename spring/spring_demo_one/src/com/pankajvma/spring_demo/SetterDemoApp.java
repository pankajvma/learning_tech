package com.pankajvma.spring_demo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class SetterDemoApp {

	public static void main(String[] args) {
		// load the spring config file
		ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
		
		// retrieval bean from spring container
//		Coach theCoach = context.getBean("myCricketCoach", Coach.class);
		CricketCoach theCoach = context.getBean("myCricketCoach", CricketCoach.class); // We can't use of Coach interface here
		
		// call methods on the bean
		System.out.println(theCoach.getDailyWorkout());
		
		System.out.println(theCoach.getDailyFortune());
		
		// call methods on the bean to print literal values
		System.out.println(theCoach.getTeam());
		
		System.out.println(theCoach.getEmailAddress());
		
		// close the context
		context.close();
	}

}
