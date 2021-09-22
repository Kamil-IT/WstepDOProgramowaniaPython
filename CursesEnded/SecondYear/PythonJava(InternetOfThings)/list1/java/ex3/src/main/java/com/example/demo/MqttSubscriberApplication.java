package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.stereotype.Component;

@SpringBootApplication
public class MqttSubscriberApplication {

    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(MqttSubscriberApplication.class, args);

        context.getBean(TimeToMqttService.class).postMessageToTimeServer();
    }

}
