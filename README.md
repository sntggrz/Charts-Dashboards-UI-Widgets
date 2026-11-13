# Charts, Dashboards & UI Widgets

A collection of interactive components built with HTML, CSS and JavaScript: data visualizations, dashboards, tables, calendars and form widgets. Each one is a standalone page with no build step.

### 👉 [Open the live gallery](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/)

Every component runs side by side in the browser, so you can hover, filter and click around without cloning anything. It has light and dark mode.

> All data in this repository is fictional. Names, companies, emails and numbers are made up for demonstration.

---

## Charts

Built with [ECharts](https://echarts.apache.org) 5.6.

| Component | What it shows | Links |
|---|---|---|
| **Stacked line** | Multiple series over a week | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/line-stack.html) · [Code](charts/line-stack.html) |
| **Area with goal line** | Progress against a target | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/area-simple.html) · [Code](charts/area-simple.html) |
| **Live data** | Line chart that updates in real time | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/dynamic-data.html) · [Code](charts/dynamic-data.html) |
| **Sprint burndown** | Ideal vs. actual remaining work | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/burndown-sprint.html) · [Code](charts/burndown-sprint.html) |
| **Bar chart** | Categories with long labels and aligned ticks | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/bar-tick-align.html) · [Code](charts/bar-tick-align.html) |
| **Ring gauge** | Single KPI at a glance | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/gauge-ring.html) · [Code](charts/gauge-ring.html) |
| **Overlapping rings** | Several KPIs in one gauge | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/gauge-ring-overlap.html) · [Code](charts/gauge-ring-overlap.html) |
| **Half gauge** | Solid gauge with a dynamic value | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/half-gauge.html) · [Code](charts/half-gauge.html) |
| **Half donut** | Share of total | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/pie-half-donut.html) · [Code](charts/pie-half-donut.html) |
| **Progress bar** | Goal tracking with an overflow state | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/progress-bar.html) · [Code](charts/progress-bar.html) |
| **Treemap** | Hierarchical proportions | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/treemap-simple.html) · [Code](charts/treemap-simple.html) |
| **Text & labels** | Typography and label experiments | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/charts/text-labels.html) · [Code](charts/text-labels.html) |

## Dashboards

Built with [Chart.js](https://www.chartjs.org) 4.

| Component | What it shows | Links |
|---|---|---|
| **Support tickets** | KPIs plus volume by date, status and type, with filters | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/dashboards/tickets-by-status.html) · [Code](dashboards/tickets-by-status.html) |

## Tables

Vanilla JavaScript.

| Component | What it shows | Links |
|---|---|---|
| **Materials with margins** | Grouped rows with cost, sale and margin totals | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/tables/materials-grouped.html) · [Code](tables/materials-grouped.html) |
| **Activities & subactivities** | Nested tasks with owners, priorities and due dates | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/tables/activities.html) · [Code](tables/activities.html) |
| **Clients** | Search, sort, copy email and row actions | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/tables/clients.html) · [Code](tables/clients.html) |

## Calendars & pickers

| Component | What it shows | Links |
|---|---|---|
| **Requests calendar** | Month view with a status per day | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/calendars/calendar.html) · [Code](calendars/calendar.html) |
| **Time picker** | Clock-style hour and minute selection | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/calendars/time-picker.html) · [Code](calendars/time-picker.html) |

## Widgets

| Component | What it shows | Links |
|---|---|---|
| **Signature pad** | Draw, clear and export a signature (mouse or touch) | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/widgets/signature-pad.html) · [Code](widgets/signature-pad.html) |
| **Threshold slider** | Traffic-light ranges with two handles | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/widgets/threshold-slider.html) · [Code](widgets/threshold-slider.html) |
| **Price range** | Min / max range input | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/widgets/price-range.html) · [Code](widgets/price-range.html) |

## QR scanning

| Component | What it shows | Links |
|---|---|---|
| **QR from image** | Upload a picture and decode it in the browser | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/qr/image-scanner.html) · [Code](qr/image-scanner.html) |
| **Camera scanner** | Live scanning with the device camera | [Live](https://sntggrz.github.io/Charts-Dashboards-UI-Widgets/qr/camera-scanner.html) · [Code](qr/camera-scanner.html) |
| **Decoding service** | Small Flask API that decodes QR images server-side | [Code](qr/qr_decoder.py) |

---

## Embedding the widgets

The widgets don't depend on any backend. When the user does something (saves a signature, picks a time, opens a calendar day, clicks a row action), the widget fires a `widget:action` event. Inside an iframe, it also posts that event to the parent page:

```js
window.addEventListener('message', (e) => {
  if (e.data?.type === 'widget:action') {
    console.log(e.data.action, e.data.payload); // e.g. "save-time", { hour: 9, minute: "30", period: "AM" }
  }
});
```

That makes them easy to plug into any app or platform.

## Running locally

Libraries load from public CDNs, so you need an internet connection.

```bash
git clone https://github.com/sntggrz/Charts-Dashboards-UI-Widgets.git
cd Charts-Dashboards-UI-Widgets
python3 -m http.server 8000
```

Then open `http://localhost:8000`. The QR service in `qr/qr_decoder.py` needs Python with `flask`, `pyzbar` and `Pillow`.
