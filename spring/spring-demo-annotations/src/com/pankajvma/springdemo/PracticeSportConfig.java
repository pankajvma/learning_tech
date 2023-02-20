package com.pankajvma.springdemo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration	// Annotation to create an empty configuration
// @ComponentScan("com.pankajvma.springdemo")	// This annotation will scan all the classes under his package and register them in the Spring Container
@PropertySource("classpath:sport.properties")
public class PracticeSportConfig {

	// define bean for our happyFortuneService
	@Bean
	public FortuneService lovelyFortuneService() {
		return new LovelyFortuneService();
	}
	
	// define bean for our Swim Coach AND inject dependency
	@Bean
	public Coach khoKhoCoach() {
		return new KhoKhoCoach(lovelyFortuneService());
	}
}