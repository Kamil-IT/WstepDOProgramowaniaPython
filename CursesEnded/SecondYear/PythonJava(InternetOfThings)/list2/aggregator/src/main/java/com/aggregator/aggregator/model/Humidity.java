package com.aggregator.aggregator.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Humidity extends DateDelivery {

    private Float id;
    private Float time;
    @JsonProperty("Humidity")
    private Float humidity;

    @Override
    public String toString() {
        return "Humidity{" +
                "id=" + id +
                ", time=" + time +
                ", humidity=" + humidity +
                '}';
    }
}
