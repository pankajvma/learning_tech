package com.pankajvma.springdemo;

import java.util.Random;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class RandomFortuneService implements FortuneService {
	
	@Value("${foo.fortuneList}")
	String[] fortunes;

	@Override
	public String getFortune() {
//		for(String fortune : fortunes)
//			System.out.println(fortune);
		return fortunes[new Random().nextInt(this.fortunes.length)];
	}

}