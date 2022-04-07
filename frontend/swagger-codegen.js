const { codegen } = require("swagger-axios-codegen");
codegen({
    remoteUrl: "http://localhost:8000/openapi",
    outputDir: "./src/shared/http",
    useStaticMethod: true,
    fileName: "api.ts",
});
