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
public class PhoneLocation extends DateDelivery {

    @JsonProperty("Latitude")
    private Double latitude;
    @JsonProperty("Longitude")
    private Double longitude;

    @Override
    public String toString() {
        return "PhoneLocation{" +
                "latitude=" + latitude +
                ", longitude=" + longitude +
                '}';
    }
}
