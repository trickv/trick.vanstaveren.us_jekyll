# Privacy Policy - rdzSonde

**Last updated:** 2026-06-07
**Publisher:** Patrick van Staveren
**Contact:** trick@vanstaveren.us

This policy describes how the rdzSonde mobile application ("the app") handles
your information. The app is open source; the source code is available at
<https://github.com/rdzSonde/rdzwx-go>.

## Summary

- rdzSonde does **not** have a user-account system. You do not create an
  account, log in, or provide any personal identifier to use the app.
- rdzSonde does **not** include advertising, analytics, crash reporting,
  fingerprinting, or any third-party tracking SDK.
- rdzSonde does **not** transmit your data to the publisher. We do not
  operate a backend server and we receive nothing about you or your usage.
- rdzSonde uses your device's location only on-device, except in the
  optional and clearly identified case where you explicitly send your GPS
  position to your own TTGO radiosonde receiver on your local network.
- A small number of clearly identified third-party services are contacted
  for specific, optional features (version check, landing prediction,
  optional Radiosondy.info login). These are described in detail below.

## What data the app accesses

### Location (GPS)

When you grant the app permission to access your location, the app uses
your latitude and longitude to:

- Center and orient the map view around you.
- Calculate distances and bearings between you and tracked radiosondes.
- Optionally transmit your position to your own TTGO ESP32 radiosonde
  receiver over your local network, so the device can compute relative
  bearings to balloons it hears. This transmission is to a device you own
  and configure; it does not leave your local network and is not visible
  to the publisher or any third party.

Your location is **not** transmitted to the publisher or to any cloud
service operated by the publisher. The most recent location is cached on
your device in browser local storage so the map can re-center quickly
when you re-open the app; you can clear this by uninstalling the app or
clearing the app's storage in your device settings.

You can deny or revoke location permission at any time through your
device's system settings. The app will continue to function with reduced
features (you will see radiosondes on the map but not their distance from
your position).

### Local network access (iOS)

On iOS, the app requests local network access in order to:

- Discover your TTGO radiosonde receiver via mDNS / Bonjour
  (`_jsonrdz._tcp` service).
- Connect to that receiver over TCP to read sonde data.

This permission is used only to communicate with devices on your own
local network. No data is transmitted to the publisher.

## Third-party services the app may contact

The following services are contacted by the app under specific conditions.
Each is operated by a third party, with its own privacy practices, which
we do not control.

### GitHub (version check)

- **What:** The app checks <https://raw.githubusercontent.com/dl9rdz/rdzwx-go/main/version.json>
  at startup to see whether a newer version is available.
- **Data sent:** A standard HTTPS request. GitHub may log standard server
  request metadata (IP address, user agent, timestamp).
- **Used for:** Notifying you when a newer version of the app has been
  released.
- **Privacy policy:** <https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement>

### Sondehub Tawhiri API (landing prediction)

- **What:** When you request a landing-point prediction for a tracked
  radiosonde, the app sends the sonde's current position, altitude, and
  ascent/descent rate to <https://api.v2.sondehub.org/tawhiri>.
- **Data sent:** Information about the radiosonde (not about you).
- **Used for:** Returning a predicted landing location.
- **Not sent:** Your location, identity, or any other personal data.
- **Operator:** Sondehub, an open community project. Their privacy and
  usage information is available at <https://sondehub.org>.

### Map tile servers (if online maps are used)

- **What:** When you use online maps (rather than the offline `.map`
  files supported on Android), the map library fetches image tiles from
  the tile server configured in the app, typically OpenStreetMap or a
  similar provider.
- **Data sent:** Standard HTTPS tile requests containing tile coordinates
  derived from the map area you are viewing. The publisher does not
  receive or log this.
- **Used for:** Displaying the map background.
- **Operator:** OpenStreetMap or whichever tile provider is configured.

## Information stored on your device

The following information is stored locally on your device, in browser
local storage. It never leaves your device and is not transmitted to the
publisher.

- The most recent GPS position the app saw, so the map can re-center
  quickly on launch.
- Your connection-mode preference (automatic mDNS discovery vs. manual
  address) for connecting to a TTGO receiver.
- The manual TTGO address you last entered, if any.

On Android, you may also select offline map files (Mapsforge `.map`
files) from your device storage. These remain on your device.

You can clear all locally stored data by uninstalling the app or by
clearing the app's storage through your device's system settings.

## Children

The app is not directed at children under 13 and does not knowingly
collect any information from children.

## Data the publisher receives

None. The publisher does not operate any backend, analytics pipeline,
crash-reporting service, or telemetry endpoint connected to this app.
The publisher has no records of who has installed the app, where it has
been installed, or how it is used.

## Changes to this policy

If the app's data practices change in a future version, this policy will
be updated and the change reflected in the "Last updated" date at the
top. Material changes will be noted in the app's release notes.

## Contact

Questions about this policy or about the app's data handling:

Patrick van Staveren
<trick@vanstaveren.us>
<https://github.com/rdzSonde/rdzwx-go>
