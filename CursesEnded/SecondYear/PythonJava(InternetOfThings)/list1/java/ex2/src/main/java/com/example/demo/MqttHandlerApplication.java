package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;

@SpringBootApplication
@EnableScheduling
public class MqttHandlerApplication {

    public static void main(String[] args) {
        SpringApplication.run(MqttHandlerApplication.class, args);
    }

}
