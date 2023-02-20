package com.pankajvma.springdemo;

import org.springframework.stereotype.Component;

@Component
public class LovelyFortuneService implements FortuneService {

	@Override
	public String getFortune() {
		// TODO Auto-generated method stub
		return "Beware of the pebbles";
	}

}
