am5.ready(function() {

    // Create root and chart
    var root = am5.Root.new("chartdiv");

    root.setThemes([
        am5themes_Animated.new(root)
    ]);

    var chart = root.container.children.push(am5map.MapChart.new(root, {
        panX: "rotateX",
        panY: "rotateY",
        projection: am5map.geoOrthographic()
    }));

    // Create polygon series for countries
    var polygonSeries = chart.series.push(am5map.MapPolygonSeries.new(root, {
        geoJSON: am5geodata_worldLow
    }));

    polygonSeries.mapPolygons.template.setAll({
        tooltipText: "{name}",
        toggleKey: "active",
        interactive: true
    });

    polygonSeries.mapPolygons.template.states.create("hover", {
        fill: am5.color(0x677935)
    });

    polygonSeries.mapPolygons.template.states.create("active", {
        fill: am5.color(0x677935)
    });

    // Create a series for graticules
    var graticuleSeries = chart.series.push(am5map.GraticuleSeries.new(root, {}));
    graticuleSeries.mapLines.template.setAll({
        stroke: am5.color(0x000000),
        strokeOpacity: 0.1
    });

    // Add zoom control
    chart.set("zoomControl", am5map.ZoomControl.new(root, {}));

    // Make stuff animate on load
    chart.appear(1000, 100);

}); // end am5.ready()
