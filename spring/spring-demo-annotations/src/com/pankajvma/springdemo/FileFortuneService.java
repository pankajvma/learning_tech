package com.pankajvma.springdemo;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

import javax.annotation.PostConstruct;

import org.springframework.stereotype.Component;

@Component
public class FileFortuneService implements FortuneService {
	
	private List<String> fortuneServices;
	
	public FileFortuneService() {
		System.out.println(">> inside FileFortuneService constructor");
	}
	@PostConstruct
	public void addFileFortunes() {
		System.out.println(">> inside addFileFortunes init method");
		File file = new File("C:\\Users\\Lenovo\\eclipse-workspace\\spring-demo-annotations\\src\\fortunes.txt");
		fortuneServices = new ArrayList<>();
		try {
			Scanner scanner = new Scanner(new FileReader(file));
			while(scanner.hasNextLine()) {
				fortuneServices.add(scanner.nextLine());
			} scanner.close();
			System.out.println(fortuneServices);
		} catch(FileNotFoundException e) {
			System.out.println(e);
		}
	}
	@Override
	public String getFortune() {
//		return "hello";
		return fortuneServices.get(new Random().nextInt(fortuneServices.size()));
	}

}
