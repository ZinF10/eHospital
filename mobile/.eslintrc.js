const globals = require('globals');
const pluginJs = require('@eslint/js');
const pluginReactConfig = require('eslint-plugin-react/configs/recommended.js');

module.exports = {
	root: true,
	extends: [
		'eslint:recommended',
		'plugin:react/recommended',
		'plugin:react-native/all',
	],
	plugins: ['react', 'react-native', 'import'],
	settings: {
		'import/resolver': {
			node: {
				paths: ['./src/'],
				alias: {
					'@/*': './src/*',
				},
			},
		},
	},
	env: {
		es2020: true,
		browser: true,
	},
	parserOptions: {
		ecmaFeatures: {
			jsx: true,
		},
	},
	overrides: [
		{
			files: ['**/*.js'],
			options: {
				globals: globals.browser,
			},
		},
		{
			files: ['**/*.jsx'],
			options: {
				parserOptions: {
					ecmaFeatures: {
						jsx: true,
					},
				},
			},
		},
	],
	...pluginJs.configs.recommended,
	...pluginReactConfig,
};
