package com.pankajvma.spring_demo;

import java.util.Random;

public class RandomFortuneService implements FortuneService {

	@Override
	public String getFortune() {
		String[] fortunes = {"You will be the top scorrer.", "You will take a hat-trick", "You are the star today"};
		return fortunes[new Random().nextInt(fortunes.length)];
	}

}