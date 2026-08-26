let config = {
	address: "0.0.0.0",
	port: 8080,
	basePath: "/",

	ipWhitelist: [],

	useHttps: false,
	httpsPrivateKey: "",
	httpsCertificate: "",

	language: "en",
	locale: "en-US",

	logLevel: ["INFO", "LOG", "WARN", "ERROR"],
	timeFormat: 12,
	units: "metric",

	modules: [

		{
			module: "MMM-BackgroundSlideshow",
			position: "fullscreen_below",
			config: {
				imagePaths: ["modules/MMM-BackgroundSlideshow/images"],
				transitionImages: true,
				randomizeImageOrder: false,
				slideshowSpeed: 10000
			}
		},

		{
			module: "alert"
		},

		{
			module: "updatenotification",
			position: "top_bar"
		},

		{
			module: "clock",
			position: "top_left"
		},

		{
			module: "calendar",
			header: "Calendar",
			position: "top_left",
			config: {
				maximumEntries: 10,
				calendars: [
					{
						fetchInterval: 7 * 24 * 60 * 60 * 1000,
						symbol: "calendar-check",
						url: "https://crispy-fortnight-p77p95qjp745h79q4-8000.app.github.dev/.ics"
					}
				]
			}
		},

		{
			module: "compliments",
			position: "lower_third",
			config: {
				compliments: {
					morning: ["Good Morning!"],
					afternoon: ["Good Afternoon!"],
					evening: ["Good Evening!"]
				}
			}
		},

		{
			module: "weather",
			position: "top_right",
			config: {
				weatherProvider: "openmeteo",
				type: "current",
				lat: 43.688,
				lon: -79.761
			}
		},

		{
			module: "weather",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				weatherProvider: "openmeteo",
				type: "forecast",
				lat: 43.688,
				lon: -79.761
			}
		},

		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "CBC News",
						url: "https://www.cbc.ca/cmlink/rss-topstories"
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true
			}
		}

	]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {
	module.exports = config;
}