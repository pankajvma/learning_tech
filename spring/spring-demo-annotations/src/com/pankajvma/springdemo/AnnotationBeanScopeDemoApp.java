package com.pankajvma.springdemo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AnnotationBeanScopeDemoApp {

	public static void main(String[] args) {
		
		// load spring config file
		ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
		
		
		// retrieve bean from spring container
		Coach theCoach = context.getBean("thatSillyCoach", Coach.class);
		
		Coach theCoach2 = context.getBean("thatSillyCoach", Coach.class);
		
		System.out.println("The bean scope is: " + (theCoach == theCoach2 ? "Singleton" : "Prototype"));
		System.out.println("Memory location for theCoach: " + theCoach);
		System.out.println("Memory location for theCoach2: " + theCoach2);
		
		// call the method on the bean
		System.out.println("\n" + theCoach.getDailyWorkout());
				
		// call method to get daily fortune
		System.out.println("\n" + theCoach.getDailyFortune());
		
		// close the context
		context.close();
	}

}
