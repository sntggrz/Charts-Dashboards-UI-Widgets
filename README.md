# Charts, Dashboards & UI Widgets

A collection of interactive components built with HTML, CSS and JavaScript: data visualizations, dashboards, tables, calendars and form widgets. Each one is a standalone page with no build step, easy to drop into any web app.

**See everything in one place:** open `index.html`. It's a live gallery where every component runs side by side.

> All data in this repository is fictional. Names, companies, emails and numbers are made up for demonstration.

## What's inside

| Folder | Contents | Built with |
|---|---|---|
| `charts/` | Stacked line, area with goal, live data, burndown, bar, gauges, half donut, progress bar, treemap | [ECharts](https://echarts.apache.org) 5.6 |
| `dashboards/` | Support tickets dashboard with KPIs, filters and linked charts | [Chart.js](https://www.chartjs.org) 4 |
| `tables/` | Grouped materials with margins and totals, nested activities, searchable clients table | Vanilla JS |
| `calendars/` | Month calendar with per-day status, clock-style time picker | Vanilla JS |
| `widgets/` | Signature pad, threshold slider, price range | Vanilla JS, Canvas |
| `qr/` | QR decoding from an image or the camera, plus a small Flask decoding service | qr-scanner, html5-qrcode, pyzbar |

## Running locally

Libraries load from public CDNs, so you need an internet connection. Serve the folder and open the gallery:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

> macOS Quick Look (Space in Finder) and GitHub's file view don't run JavaScript, so the pages look empty there. Open them in a browser or through GitHub Pages instead.

To publish the gallery: **Settings → Pages → Deploy from branch → `main` / root**.

The QR service in `qr/qr_decoder.py` needs Python with `flask`, `pyzbar` and `Pillow`.

## Embedding the widgets

Interactive widgets don't depend on any backend. When the user does something (saves a signature, picks a time, opens a calendar day, clicks a row action), the widget fires a `widget:action` event on `window`. If the widget is inside an iframe, it also posts that event to the parent page:

```js
window.addEventListener('message', (e) => {
  if (e.data?.type === 'widget:action') {
    console.log(e.data.action, e.data.payload); // e.g. "save-time", { hour: 9, minute: "30", period: "AM" }
  }
});
```

That makes them easy to connect to any app or platform.
