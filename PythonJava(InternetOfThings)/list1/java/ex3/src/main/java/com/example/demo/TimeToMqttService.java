package com.example.demo;

import com.google.gson.Gson;
import org.eclipse.paho.client.mqttv3.IMqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.springframework.http.*;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.*;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReference;

@Service
public class TimeToMqttService {

    public static final String TOPIC_MAIN = "test-java-spring-test";
    private IMqttClient iMqttClient;

    public TimeToMqttService(IMqttClient iMqttClient) {
        this.iMqttClient = iMqttClient;
    }


    public String subscribeMessagesFromMqtt(String topic, int waitMillis) throws MqttException {
        AtomicReference<String> messages = new AtomicReference<>("");
        CountDownLatch countDownLatch = new CountDownLatch(10);
        iMqttClient.subscribeWithResponse(topic, (topicMessage, message) -> {
            messages.set(new String(message.getPayload()));
            countDownLatch.countDown();
        });

        try {
            countDownLatch.await(waitMillis, TimeUnit.MILLISECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return messages.get();
    }

    public void postMessageToTimeServer(String time, List<String> students){
        String url = "http://localhost:8080/time";
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));

        Request requestObj = new Request(students, time);
        Gson gson = new Gson();
        String json = gson.toJson(requestObj);
        HttpEntity<String> request = new HttpEntity<>(json, headers);
        ResponseEntity<String> response = restTemplate.postForEntity(
                url,
                request,
                String.class);
        if (response.getStatusCode() == HttpStatus.OK) {
            System.out.println("message send: " + time);
            System.out.println(response.getBody());
        } else {
            System.out.println("Request Failed");
            System.out.println(response.getStatusCode());
        }
    }


    public void postMessageToTimeServer() {
        try {
            String time = subscribeMessagesFromMqtt(TOPIC_MAIN, 10000);
            postMessageToTimeServer(time, Arrays.asList("nr_indeksu1", "nr_indeksu2"));
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }
}
