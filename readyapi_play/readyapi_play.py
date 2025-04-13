from __future__ import annotations

import json
from enum import Enum
from typing_extensions import Annotated, Doc
from readyapi.responses import HTMLResponse


class Layout(Enum):
    MODERN = "modern"
    CLASSIC = "classic"


class SearchHotKey(Enum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"
    H = "h"
    I = "i"
    J = "j"
    K = "k"
    L = "l"
    M = "m"
    N = "n"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    S = "s"
    T = "t"
    U = "u"
    V = "v"
    W = "w"
    X = "x"
    Y = "y"
    Z = "z"


play_theme = """
/* basic theme */
.light-mode {
  --play-color-1: #2a2f45;
  --play-color-2: #757575;
  --play-color-3: #8e8e8e;
  --play-color-accent: #009485;

  --play-background-1: #fff;
  --play-background-2: #fcfcfc;
  --play-background-3: #f8f8f8;
  --play-background-accent: #ecf8f6;

  --play-border-color: rgba(0, 0, 0, 0.1);
}
.dark-mode {
  --play-color-1: rgba(255, 255, 255, 0.9);
  --play-color-2: rgba(255, 255, 255, 0.62);
  --play-color-3: rgba(255, 255, 255, 0.44);
  --play-color-accent: #00ccb8;

  --play-background-1: #1f2129;
  --play-background-2: #282a35;
  --play-background-3: #30323d;
  --play-background-accent: #223136;

  --play-border-color: rgba(255, 255, 255, 0.1);
}
/* Document Sidebar */
.light-mode .t-doc__sidebar {
  --sidebar-background-1: var(--play-background-1);
  --sidebar-item-hover-color: currentColor;
  --sidebar-item-hover-background: var(--play-background-2);
  --sidebar-item-active-background: var(--play-background-accent);
  --sidebar-border-color: var(--play-border-color);
  --sidebar-color-1: var(--play-color-1);
  --sidebar-color-2: var(--play-color-2);
  --sidebar-color-active: var(--play-color-accent);
  --sidebar-search-background: transparent;
  --sidebar-search-border-color: var(--play-border-color);
  --sidebar-search--color: var(--play-color-3);
}

.dark-mode .sidebar {
  --sidebar-background-1: var(--play-background-1);
  --sidebar-item-hover-color: currentColor;
  --sidebar-item-hover-background: var(--play-background-2);
  --sidebar-item-active-background: var(--play-background-accent);
  --sidebar-border-color: var(--play-border-color);
  --sidebar-color-1: var(--play-color-1);
  --sidebar-color-2: var(--play-color-2);
  --sidebar-color-active: var(--play-color-accent);
  --sidebar-search-background: transparent;
  --sidebar-search-border-color: var(--play-border-color);
  --sidebar-search--color: var(--play-color-3);
}

/* advanced */
.light-mode {
  --play-button-1: rgb(49 53 56);
  --play-button-1-color: #fff;
  --play-button-1-hover: rgb(28 31 33);

  --play-color-green: #009485;
  --play-color-red: #d52b2a;
  --play-color-yellow: #ffaa01;
  --play-color-blue: #0a52af;
  --play-color-orange: #953800;
  --play-color-purple: #8251df;

  --play-scrollbar-color: rgba(0, 0, 0, 0.18);
  --play-scrollbar-color-active: rgba(0, 0, 0, 0.36);
}
.dark-mode {
  --play-button-1: #f6f6f6;
  --play-button-1-color: #000;
  --play-button-1-hover: #e7e7e7;

  --play-color-green: #00ccb8;
  --play-color-red: #e5695b;
  --play-color-yellow: #ffaa01;
  --play-color-blue: #78bffd;
  --play-color-orange: #ffa656;
  --play-color-purple: #d2a8ff;

  --play-scrollbar-color: rgba(255, 255, 255, 0.24);
  --play-scrollbar-color-active: rgba(255, 255, 255, 0.48);
}
:root {
  --play-radius: 3px;
  --play-radius-lg: 6px;
  --play-radius-xl: 8px;
}
.play-card:nth-of-type(3) {
  display: none;
}"""

def get_play_api_reference(
    *,
    openapi_url: Annotated[
        str,
        Doc(
            """
            The OpenAPI URL that Play should load and use.
            This is normally done automatically by ReadyAPI using the default URL
            `/openapi.json`.
            """
        ),
    ],
    title: Annotated[
        str,
        Doc(
            """
            The HTML `<title>` content, normally shown in the browser tab.
            """
        ),
    ],
    play_js_url: Annotated[
        str,
        Doc(
            """
            The URL to use to load the Play JavaScript.
            It is normally set to a CDN URL.
            """
        ),
    ] = "https://cdn.jsdelivr.net/npm/@play/api-reference",
    play_proxy_url: Annotated[
        str,
        Doc(
            """
            The URL to use to set the Play Proxy.
            It is normally set to a Play API URL (https://proxy.play.com), but default is empty
            """
        ),
    ] = "",
    play_favicon_url: Annotated[
        str,
        Doc(
            """
            The URL of the favicon to use. It is normally shown in the browser tab.
            """
        ),
    ] = "https://readyapi.tiangolo.com/img/favicon.png",
    play_theme: Annotated[
        str,
        Doc(
            """
            Custom CSS theme for Play.
            """
        ),
    ] = play_theme,
    layout: Annotated[
        Layout,
        Doc(
            """
            The layout to use for Play.
            Default is "modern".
            """
        ),
    ] = Layout.MODERN,
    show_sidebar: Annotated[
        bool,
        Doc(
            """
            A boolean to show the sidebar.
            Default is True which means the sidebar is shown.
            """
        ),
    ] = True,
    hide_download_button: Annotated[
        bool,
        Doc(
            """
            A boolean to hide the download button.
            Default is False which means the download button is shown.
            """
        ),
    ] = False,
    hide_models: Annotated[
        bool,
        Doc(
            """
            A boolean to hide all models.
            Default is False which means all models are shown.
            """
        ),
    ] = False,
    dark_mode: Annotated[
        bool,
        Doc(
            """
            Whether dark mode is on or off initially (light mode).
            Default is True which means dark mode is used.
            """
        ),
    ] = True,
    search_hot_key: Annotated[
        SearchHotKey,
        Doc(
            """
            The hotkey to use for search.
            Default is "k" (e.g. CMD+k).
            """
        ),
    ] = SearchHotKey.K,
    hidden_clients: Annotated[
        bool | dict[str, bool | list[str]] | list[str],
        Doc(
            """
            A dictionary with the keys being the target names and the values being a boolean to hide all clients of the target or a list clients.
            If a boolean is provided, it will hide all the clients with that name.
            Backwards compatibility: If a list of strings is provided, it will hide the clients with the name and the list of strings.
            Default is [] which means no clients are hidden.
            """
        ),
    ] = [],
    servers: Annotated[
        list[dict[str, str]],
        Doc(
            """
            A list of dictionaries with the keys being the server name and the value being the server URL.
            Default is [] which means no servers are provided.
            """
        ),
    ] = [],
    default_open_all_tags: Annotated[
        bool,
        Doc(
            """
            A boolean to open all tags by default.
            Default is False which means all tags are closed by default.
            """
        ),
    ] = False,
    authentication: Annotated[
        dict,
        Doc(
            """
            A dictionary of additional authentication information.
            Default is {} which means no authentication information is provided.
            """
        ),
    ] = {},
    integration: Annotated[
        str | None,
        Doc(
            """
            The integration type. Default is 'readyapi'.
            Set to None or a different value to override.
            """
        ),
    ] = 'readyapi',
) -> HTMLResponse:
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>{title}</title>
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="{play_favicon_url}">
    <style>
      body {{
        margin: 0;
        padding: 0;
      }}
    </style>
    <style>
    {play_theme}
    </style>
    </head>
    <body>
    <noscript>
        Play requires Javascript to function. Please enable it to browse the documentation.
    </noscript>
    <script
      id="api-reference"
      data-url="{openapi_url}"
      data-proxy-url="{play_proxy_url}"></script>
    <script>
      var configuration = {{
        layout: "{layout.value}",
        showSidebar: {json.dumps(show_sidebar)},
        hideDownloadButton: {json.dumps(hide_download_button)},
        hideModels: {json.dumps(hide_models)},
        darkMode: {json.dumps(dark_mode)},
        searchHotKey: "{search_hot_key.value}",
        hiddenClients: {json.dumps(hidden_clients)},
        servers: {json.dumps(servers)},
        defaultOpenAllTags: {json.dumps(default_open_all_tags)},
        authentication: {json.dumps(authentication)},
        _integration: {json.dumps(integration)},
      }}

      document.getElementById('api-reference').dataset.configuration =
        JSON.stringify(configuration)
    </script>
    <script src="{play_js_url}"></script>
    </body>
    </html>
    """
    return HTMLResponse(html)
