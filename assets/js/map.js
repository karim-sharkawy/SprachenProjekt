
// am5.ready(function() {
//     // Create root element
//     var root = am5.Root.new("chartdiv");

//     // Set themes
//     root.setThemes([
//         am5themes_Animated.new(root)
//     ]);

//     // Create the map chart
//     var chart = root.container.children.push(am5map.MapChart.new(root, {
//         panX: "translateX",
//         panY: "translateY",
//         projection: am5map.geoMercator()
//     }));

//     // Create main polygon series for countries
//     var polygonSeries = chart.series.push(am5map.MapPolygonSeries.new(root, {
//         geoJSON: am5geodata_worldLow,
//         exclude: ["AQ"] // Exclude Antarctica
//     }));

//     polygonSeries.mapPolygons.template.setAll({
//         tooltipText: "{name}",
//         toggleKey: "active",
//         interactive: true
//     });

//     polygonSeries.mapPolygons.template.states.create("hover", {
//         fill: root.interfaceColors.get("primaryButtonHover")
//     });

//     polygonSeries.mapPolygons.template.states.create("active", {
//         fill: root.interfaceColors.get("primaryButtonHover")
//     });

//     var previousPolygon;
//     polygonSeries.mapPolygons.template.on("active", function (active, target) {
//         if (previousPolygon && previousPolygon !== target) {
//             previousPolygon.set("active", false);
//         }
//         if (target.get("active")) {
//             polygonSeries.zoomToDataItem(target.dataItem);
//         } else {
//             chart.goHome();
//         }
//         previousPolygon = target;
//     });

//     // Add zoom control
//     var zoomControl = chart.set("zoomControl", am5map.ZoomControl.new(root, {}));
//     zoomControl.homeButton.set("visible", true);

//     // Set clicking on "water" to zoom out
//     chart.chartContainer.get("background").events.on("click", function () {
//         chart.goHome();
//     });

//     // Make stuff animate on load
//     chart.appear(1000, 100);
// }); // end am5.ready()

