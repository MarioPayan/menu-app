import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';
import eslintConfigPrettier from "eslint-config-prettier";
// import eslintPluginReact from "eslint-plugin-react";
// import eslintConfigNext from "eslint-config-next";

const updateConfig = (config) => {
  const globalConfig = {
    replace: {
      files: ["src/**/*.ts", "src/**/*.tsx"],
    },
    extend: {},
  }
  return {
    ...config,
    ...globalConfig.replace
  }
}

const eslintConfig = [
  updateConfig(eslintConfigPrettier),
  // updateConfig(eslintPluginReact.configs.recommended),
  // updateConfig(eslintConfigNext),
  updateConfig(eslint.configs.all),
  updateConfig(...tseslint.configs.strictTypeChecked),
  {
    files: ["src/**/*.ts", "src/**/*.tsx"],
    rules: {},
    languageOptions: {
      globals: {
        React: "readonly",
        JSX: "readonly",
        fetch: "readonly",
        console: "readonly",

      },
      parserOptions: {
        ecmaVersion: 2022,
        sourceType: "module",
        parser: "@typescript-eslint/parser",
      }
    }
  }
];

export default eslintConfig