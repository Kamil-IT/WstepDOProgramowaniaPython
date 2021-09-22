package com.aggregator.aggregator;

import com.aggregator.aggregator.model.*;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

public class Service <Entity extends DateDelivery> {

    private List<Entity> entities = new ArrayList<>();

    void addEntity(Entity entity){
        entity.setDate(new Date());
        entities.add(entity);
    }

    List<Entity> getEntities(){
        return entities;
    }

    List<Entity> getEntitiesAfter(Date date){
        return entities.stream()
                .filter(e ->
                        e.getDate().after(date)
                )
                .collect(Collectors.toList());
    }
}
