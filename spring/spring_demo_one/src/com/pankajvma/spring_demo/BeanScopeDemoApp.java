package com.pankajvma.spring_demo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class BeanScopeDemoApp {

	public static void main(String[] args) {
		// TODO load the spring configuration file
		ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("beanScope-applicationContext.xml");
		
		// TODO retrieve bean from Spring container
		Coach theCoach = context.getBean("myCoach", Coach.class);
		
		Coach alphaCoach = context.getBean("myCoach", Coach.class);
		
		// check if both objects are same
		System.out.println("Pointing to the same object: " + (theCoach==alphaCoach));
		System.out.println("Memory location of theCoach: " + theCoach);
		System.out.println("Memory location of alphaCoach: " + alphaCoach);

		// close the context
		context.close(); // for prototype scoped beans, spring does not call the destroy method
	}

}