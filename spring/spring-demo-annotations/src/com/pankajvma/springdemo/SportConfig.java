package com.pankajvma.springdemo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration	// Annotation to create an empty configuration
// @ComponentScan("com.pankajvma.springdemo")	// This annotation will scan all the classes under his package and register them in the Spring Container
@PropertySource("classpath:sport.properties")
public class SportConfig {

	// define bean for our happyFortuneService
	@Bean
	public FortuneService happyFortuneService() {
		return new HappyFortuneService();
	}
	
	// define bean for our Swim Coach AND inject dependency
	@Bean
	public Coach swimCoach() {
		return new SwimCoach(happyFortuneService());
	}
}