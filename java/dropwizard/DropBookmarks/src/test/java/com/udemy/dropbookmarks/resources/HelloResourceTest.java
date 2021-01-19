package com.udemy.dropbookmarks.resources;
import io.dropwizard.testing.junit.ResourceTestRule;
import org.junit.*;
import org.junit.jupiter.api.Assertions;

import javax.annotation.Resource;
import javax.print.attribute.standard.Media;
import javax.ws.rs.core.MediaType;

public class HelloResourceTest {

    @ClassRule
    public static final ResourceTestRule RULE = ResourceTestRule
            .builder()
            .addResource(new HelloResource())
            .build();

    public HelloResourceTest() {

    }

    @Test
     public void testGetGreeting() {
        String expected = "<b>Hello Rikesh2<b>";
        String actual = RULE
                .getJerseyTest()
                .target("/greeting")
                .request(MediaType.TEXT_HTML)
                .get(String.class);
        System.out.println ("expected: " + expected);
        System.out.println ("actual: " + actual);
        Assertions.assertEquals(expected,actual);
    }


}