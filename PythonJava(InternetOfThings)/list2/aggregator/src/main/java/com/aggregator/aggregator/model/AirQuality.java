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
public class AirQuality extends DateDelivery {

    @JsonProperty("Nitrogen Dioxide Micrograms Per Cubic Metre")
    private double NitrogenDioxideMicrogramsPerCubicMetre;

    @Override
    public String toString() {
        return "AirQuality{" +
                "NitrogenDioxideMicrogramsPerCubicMetre=" + NitrogenDioxideMicrogramsPerCubicMetre +
                '}';
    }
}
