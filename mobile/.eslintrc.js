module.exports = {
  root: true,
  extends: ['@react-native', 'prettier', 'prettier/react'],
  plugins: ['prettier'],
  rules: {
    'prettier/prettier': 'warn',
    'react-native/no-inline-styles': 'off',
  },
};
