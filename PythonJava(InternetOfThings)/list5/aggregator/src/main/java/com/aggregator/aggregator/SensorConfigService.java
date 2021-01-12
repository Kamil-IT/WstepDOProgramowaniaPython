package com.aggregator.aggregator;

import com.aggregator.aggregator.model.Configuration;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.net.URL;
import java.util.Map;

@Service
public class SensorConfigService {

    private ObjectMapper objectMapper = new ObjectMapper();

    public Configuration getApp1Config() {
        try {
            return objectMapper.readValue(new URL("http://localhost:5001/config"), Configuration.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public Configuration getApp2Config() {
        try {
            return objectMapper.readValue(new URL("http://localhost:5002/config"), Configuration.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public Configuration getApp3Config() {
        try {
            return objectMapper.readValue(new URL("http://localhost:5003/config"), Configuration.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public Configuration getApp4Config() {
        try {
            return objectMapper.readValue(new URL("http://localhost:5004/config"), Configuration.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public Configuration getApp5Config() {
        try {
            return objectMapper.readValue(new URL("http://localhost:5005/config"), Configuration.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void postApp1Config(Map<String, String> stringMap) {
        RestTemplate restTemplate = new RestTemplate();
        restTemplate.postForEntity("http://localhost:5001/config", stringMap, String.class);
    }

    public void postApp2Config(Map<String, String> stringMap) {
        RestTemplate restTemplate = new RestTemplate();
        restTemplate.postForEntity("http://localhost:5002/config", stringMap, String.class);
    }

    public void postApp3Config(Map<String, String> stringMap) {
        RestTemplate restTemplate = new RestTemplate();
        restTemplate.postForEntity("http://localhost:5003/config", stringMap, String.class);
    }

    public void postApp4Config(Map<String, String> stringMap) {
        RestTemplate restTemplate = new RestTemplate();
        restTemplate.postForEntity("http://localhost:5004/config", stringMap, String.class);
    }

    public void postApp5Config(Map<String, String> stringMap) {
        RestTemplate restTemplate = new RestTemplate();
        restTemplate.postForEntity("http://localhost:5005/config", stringMap, String.class);
    }
}
