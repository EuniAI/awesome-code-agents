import fs from "node:fs";
import { JSDOM } from "jsdom";
import { optimize } from "svgo";
import XYChart from "../shared/packages/xy-chart.js";
import { convertDataToChartData, getRepoData } from "../shared/common/chart.js";
import { fixJsdomSvgCasing, getChartWidthWithSize, getBase64Image } from "./utils.js";

const token = process.env.GH_TOKEN || "";
const repo = process.env.REPO || "euniai/awesome-code-agents";
const size = "laptop";

const data = await getRepoData([repo], token, 16);
await Promise.all(data.map(async (d: any) => {
  try { d.logoUrl = await getBase64Image(`${d.logoUrl}&size=22`); } catch { d.logoUrl = ""; }
}));

const dom = new JSDOM(`<!DOCTYPE html><body></body>`);
const doc = dom.window.document;
const svg = doc.createElement("svg") as any;
doc.querySelector("body")!.append(svg);
svg.setAttribute("width", `${getChartWidthWithSize(size)}`);
svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");

XYChart(svg,
  { title: "Star History", xLabel: "Date", yLabel: "GitHub Stars",
    data: convertDataToChartData(data, "Date"),
    showDots: false, transparent: false, theme: "light" },
  { xTickLabelType: "Date", chartWidth: getChartWidthWithSize(size),
    useLogScale: false, legendPosition: "top-left" });

const out = optimize(fixJsdomSvgCasing(svg.outerHTML), { multipass: true }).data;
fs.writeFileSync(process.env.OUT || "star-history.svg", out);
console.log(`[OK] wrote ${out.length} bytes, ${data[0].starRecords.length} points`);
