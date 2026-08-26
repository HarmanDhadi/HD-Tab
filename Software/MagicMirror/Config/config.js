<<<<<<< HEAD
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

=======
/* Config Sample
 *
 * For more information on how you can configure this file
 * see https://docs.magicmirror.builders/configuration/introduction.html
 * and https://docs.magicmirror.builders/modules/configuration.html
 *
 * You can use environment variables using a `config.js.template` file instead of `config.js`
 * which will be converted to `config.js` while starting. For more information
 * see https://docs.magicmirror.builders/configuration/introduction.html#enviromnent-variables
 */
let config = {
	address: "localhost",	// Address to listen on, can be:
							// - "localhost", "127.0.0.1", "::1" to listen on loopback interface
							// - another specific IPv4/6 to listen on a specific interface
							// - "0.0.0.0", "::" to listen on any interface
							// Default, when address config is left out or empty, is "localhost"
	port: 8080,
	basePath: "/",	// The URL path where MagicMirror² is hosted. If you are using a Reverse proxy
									// you must set the sub path here. basePath must end with a /
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"],	// Set [] to allow all IP addresses
									// or add a specific IPv4 of 192.168.1.5 :
									// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
									// or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
									// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	useHttps: false,			// Support HTTPS or not, default "false" will use HTTP
	httpsPrivateKey: "",	// HTTPS private key path, only require when useHttps is true
	httpsCertificate: "",	// HTTPS Certificate path, only require when useHttps is true

	language: "en",
	locale: "en-US",   // this variable is provided as a consistent location
			   // it is currently only used by 3rd party modules. no MagicMirror code uses this value
			   // as we have no usage, we  have no constraints on what this field holds
			   // see https://en.wikipedia.org/wiki/Locale_(computer_software) for the possibilities

	logLevel: ["INFO", "LOG", "WARN", "ERROR"], // Add "DEBUG" for even more logging
	timeFormat: 24,
	units: "metric",

	modules: [
		{
			module: "alert",
		},
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
		{
			module: "updatenotification",
			position: "top_bar"
		},
<<<<<<< HEAD

=======
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
		{
			module: "clock",
			position: "top_left"
		},
<<<<<<< HEAD

		{
			module: "calendar",
			header: "Calendar",
			position: "top_left",
			config: {
				maximumEntries: 10,
=======
		{
			module: "calendar",
			header: "US Holidays",
			position: "top_left",
			config: {
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
				calendars: [
					{
						fetchInterval: 7 * 24 * 60 * 60 * 1000,
						symbol: "calendar-check",
<<<<<<< HEAD
						url: "https://crispy-fortnight-p77p95qjp745h79q4-8000.app.github.dev/.ics"
=======
						url: "https://ics.calendarlabs.com/76/mm3137/US_Holidays.ics"
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
					}
				]
			}
		},
<<<<<<< HEAD

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

=======
		{
			module: "compliments",
			position: "lower_third"
		},
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
		{
			module: "weather",
			position: "top_right",
			config: {
				weatherProvider: "openmeteo",
				type: "current",
<<<<<<< HEAD
				lat: 43.688,
				lon: -79.761
			}
		},

=======
				lat: 40.776676,
				lon: -73.971321
			}
		},
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
		{
			module: "weather",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				weatherProvider: "openmeteo",
				type: "forecast",
<<<<<<< HEAD
				lat: 43.688,
				lon: -79.761
			}
		},

=======
				lat: 40.776676,
				lon: -73.971321
			}
		},
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
<<<<<<< HEAD
						title: "CBC News",
						url: "https://www.cbc.ca/cmlink/rss-topstories"
=======
						title: "New York Times",
						url: "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true
			}
<<<<<<< HEAD
		}

=======
		},
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
	]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
<<<<<<< HEAD
if (typeof module !== "undefined") {
	module.exports = config;
}
=======
if (typeof module !== "undefined") { module.exports = config; }
>>>>>>> 96a5c9c1291943d990351d4ec4b2b522110461ef
