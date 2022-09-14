const config = {
	content: [
		"./src/**/*.{html,js,svelte,ts}",
		"./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}"
	],

	theme: {
		extend: {
			colors: {
				primary: "#F3FE5C",
				secondary: "#9CE8F1"
			}
		}
	},

	plugins: [require("flowbite/plugin")],
	darkMode: "class"
}

module.exports = config
