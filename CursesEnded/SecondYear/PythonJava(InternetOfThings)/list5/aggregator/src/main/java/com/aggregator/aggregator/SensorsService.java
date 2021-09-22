package com.aggregator.aggregator;

import com.aggregator.aggregator.model.*;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

public class SensorsService<Entity extends BaseEntity> {

    private List<Entity> entities = new ArrayList<>();

    void addEntity(Entity entity){
        Date date = new Date();
        entity.setDate(date);
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

    List<Entity> getEntitiesBetween(Date dateStart, Date dateEnd){
        return entities.stream()
                .filter(e ->
                        e.getDate().after(dateStart) && e.getDate().before(dateEnd)
                )
                .collect(Collectors.toList());
    }
}
