module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
  ? '/tasks'
  : '/',
  configureWebpack: {
    externals: {
      vue: 'Vue'
    },
    resolve: {
      alias: {
        'vue$': 'vue/dist/vue.esm.js', // Use the correct path to your Vue distribution
      },
    },
  },
};


const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
});
