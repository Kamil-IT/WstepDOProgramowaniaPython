package com.example.demo;

import org.eclipse.paho.client.mqttv3.IMqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class TimeToMqttService {

    public static final String TOPIC_MAIN = "test-java-spring-test";
    private IMqttClient iMqttClient;

    public TimeToMqttService(IMqttClient iMqttClient) {
        this.iMqttClient = iMqttClient;
    }

    /**
     * @param message message
     * @param qos the "quality of service" to use.  Set to 0, 1, 2.
     * @param retain whether or not the messaging engine should retain the message.
     */
    public void sendMessageToMqtt(String topic, String message, int qos, boolean retain) throws MqttException {

        MqttMessage mqttMessage = new MqttMessage(message.getBytes());
        mqttMessage.setQos(qos);
        mqttMessage.setRetained(retain);

        iMqttClient.publish(topic, mqttMessage);
    }

    public String getTimeFromTimeServer(){
        final String uri = "http://localhost:8080/time?tz=+3";
        RestTemplate restTemplate = new RestTemplate();
        String result = restTemplate.getForObject(uri, String.class);
        System.out.println("Time from server: " + result);
        return result;
    }


    @Scheduled(fixedRate = 5000)
    public void sendMessageToMqttEvery5s() {
        String message = getTimeFromTimeServer();
        try {
            sendMessageToMqtt(TOPIC_MAIN, message, 1, true);
            System.out.println("topic: " + TOPIC_MAIN + " message: " + message);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }
}
