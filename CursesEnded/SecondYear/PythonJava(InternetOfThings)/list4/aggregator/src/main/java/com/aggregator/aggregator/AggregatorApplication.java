package com.aggregator.aggregator;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Condition;
import org.springframework.context.annotation.ConditionContext;
import org.springframework.context.annotation.Conditional;
import org.springframework.core.type.AnnotatedTypeMetadata;
import org.springframework.integration.annotation.IntegrationComponentScan;
import org.springframework.integration.channel.DirectChannel;
import org.springframework.integration.core.MessageProducer;
import org.springframework.integration.mqtt.inbound.MqttPahoMessageDrivenChannelAdapter;
import org.springframework.integration.mqtt.support.DefaultPahoMessageConverter;
import org.springframework.messaging.MessageChannel;

import static com.aggregator.aggregator.MqttController.MQTT_PUBLISHER_ID;
import static com.aggregator.aggregator.MqttController.MQTT_SERVER_ADDRESS;

@SpringBootApplication
@IntegrationComponentScan
public class AggregatorApplication {

    public static final Integer MQTT_URLS = 1;

    public static void main(String[] args) {
        SpringApplication.run(AggregatorApplication.class, args);
    }

    @Bean
    public MessageChannel mqttInputChannel() {
        return new DirectChannel();
    }

    @Bean
    public MessageProducer inbound() {
        MqttPahoMessageDrivenChannelAdapter adapter =
                new MqttPahoMessageDrivenChannelAdapter(MQTT_SERVER_ADDRESS, MQTT_PUBLISHER_ID,
                        "beach_water_quality",
                        "phone_location",
                        "temperature",
                        "air-quality",
                        "humidity");
        adapter.setCompletionTimeout(5000);
        adapter.setConverter(new DefaultPahoMessageConverter());
        adapter.setQos(1);
        adapter.setOutputChannel(mqttInputChannel());
        return adapter;
    }

    @Bean
    @Conditional(OnMoreThen2MqttCondition.class)
    public MessageProducer inbound2() {
        MqttPahoMessageDrivenChannelAdapter adapter =
                new MqttPahoMessageDrivenChannelAdapter("tcp://broker.hivemq.com:1883", MQTT_PUBLISHER_ID,
                        "asjdnbkasjdbkasjbdask");
        adapter.setCompletionTimeout(5000);
        adapter.setConverter(new DefaultPahoMessageConverter());
        adapter.setQos(1);
        adapter.setOutputChannel(mqttInputChannel());
        return adapter;
    }

    @Bean
    @Conditional(OnMoreThen3MqttCondition.class)
    public MessageProducer inbound3() {
        MqttPahoMessageDrivenChannelAdapter adapter =
                new MqttPahoMessageDrivenChannelAdapter("tcp://broker.hivemq.com:1883", MQTT_PUBLISHER_ID,
                        "asjdnbkasjdbkasjbdask");
        adapter.setCompletionTimeout(5000);
        adapter.setConverter(new DefaultPahoMessageConverter());
        adapter.setQos(1);
        adapter.setOutputChannel(mqttInputChannel());
        return adapter;
    }

    @Bean
    @Conditional(OnMoreThen4MqttCondition.class)
    public MessageProducer inbound4() {
        MqttPahoMessageDrivenChannelAdapter adapter =
                new MqttPahoMessageDrivenChannelAdapter("tcp://broker.hivemq.com:1883", MQTT_PUBLISHER_ID,
                        "asjdnbkasjdbkasjbdask");
        adapter.setCompletionTimeout(5000);
        adapter.setConverter(new DefaultPahoMessageConverter());
        adapter.setQos(1);
        adapter.setOutputChannel(mqttInputChannel());
        return adapter;
    }

    @Bean
    @Conditional(OnMoreThen5MqttCondition.class)
    public MessageProducer inbound5() {
        MqttPahoMessageDrivenChannelAdapter adapter =
                new MqttPahoMessageDrivenChannelAdapter("tcp://broker.hivemq.com:1883", MQTT_PUBLISHER_ID,
                        "asjdnbkasjdbkasjbdask");
        adapter.setCompletionTimeout(5000);
        adapter.setConverter(new DefaultPahoMessageConverter());
        adapter.setQos(1);
        adapter.setOutputChannel(mqttInputChannel());
        return adapter;
    }

    static class OnMoreThen2MqttCondition implements Condition {
        @Override
        public boolean matches(
                ConditionContext context,
                AnnotatedTypeMetadata metadata) {
            return MQTT_URLS > 1;
        }
    }

    static class OnMoreThen3MqttCondition implements Condition {
        @Override
        public boolean matches(
                ConditionContext context,
                AnnotatedTypeMetadata metadata) {
            return MQTT_URLS > 2;
        }
    }

    static class OnMoreThen4MqttCondition implements Condition {
        @Override
        public boolean matches(
                ConditionContext context,
                AnnotatedTypeMetadata metadata) {
            return MQTT_URLS > 3;
        }
    }

    static class OnMoreThen5MqttCondition implements Condition {
        @Override
        public boolean matches(
                ConditionContext context,
                AnnotatedTypeMetadata metadata) {
            return MQTT_URLS > 4;
        }
    }

}
