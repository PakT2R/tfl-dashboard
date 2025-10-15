#!/usr/bin/env python3
"""
ACC Web Dashboard - Versione Minimale
Homepage + Work in Progress
"""

import streamlit as st
import json
import os
from pathlib import Path
from datetime import datetime
import base64

# Configurazione pagina
st.set_page_config(
    page_title="TFL Racing Dashboard",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="expanded"
)

class ACCMinimalDashboard:
    """Dashboard minimale - Solo Homepage + WIP"""
    
    def __init__(self):
        self.config = self.load_config()
        self.inject_custom_css()
    
    def load_config(self) -> dict:
        """Carica configurazione con fallback"""
        config_sources = ['acc_config.json', 'acc_config_d.json']
        
        default_config = {
            "community": {
                "name": os.getenv('ACC_COMMUNITY_NAME', "N/A"),
                "description": os.getenv('ACC_COMMUNITY_DESC', "N/A")
            },
            "social": {
                "discord": "",
                "simgrid": ""
            }
        }
        
        for config_file in config_sources:
            if Path(config_file).exists():
                try:
                    with open(config_file, 'r', encoding='utf-8') as f:
                        file_config = json.load(f)
                    default_config.update(file_config)
                    return default_config
                except:
                    continue
        
        return default_config
    
    def inject_custom_css(self):
        """CSS personalizzato"""
        st.markdown("""
        <style>
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #1f4e79, #2d5a87);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 4px solid #1f4e79;
            margin-bottom: 1rem;
        }
        
        .metric-value {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1f4e79;
            margin: 0;
        }
        
        .metric-label {
            font-size: 1.1rem;
            color: #666;
            margin: 0;
        }
        
        .wip-container {
            text-align: center;
            padding: 3rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            margin: 2rem 0;
            color: white;
        }
        
        @media (max-width: 768px) {
            .metric-value {
                font-size: 2rem;
            }
            .main-header h1 {
                font-size: 1.8rem;
            }
        }
        </style>
        """, unsafe_allow_html=True)
    
    def show_community_banner(self):
        """Mostra banner community"""
        try:
            banner_path = "banner.jpg"
            
            if Path(banner_path).exists():
                # Banner con immagine
                with open(banner_path, "rb") as img_file:
                    img_base64 = base64.b64encode(img_file.read()).decode()
                
                community_name = self.config['community']['name']
                
                st.markdown(f"""
                <div style="
                    background-image: url(data:image/jpeg;base64,{img_base64});
                    background-size: cover;
                    background-position: center;
                    height: 300px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    margin: 2rem 0;
                    border-radius: 15px;
                ">
                    <div style="
                        background: rgba(0,0,0,0.4);
                        padding: 2rem;
                        border-radius: 15px;
                        color: white;
                    ">
                        <h1 style="margin: 0; font-size: 3rem; font-weight: bold; 
                                   text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
                            🏁 {community_name}
                        </h1>
                        <h3 style="margin: 0.5rem 0 0 0; font-size: 1.5rem; 
                                   text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
                            ACC Server Dashboard
                        </h3>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Fallback senza immagine
                community_name = self.config['community']['name']
                st.markdown(f"""
                <div class="main-header">
                    <h1>🏁 {community_name}</h1>
                    <h3>by Terronia Racing</h3>
                </div>
                """, unsafe_allow_html=True)
            
            # Link social
            self.show_social_buttons()
            
        except Exception as e:
            st.error(f"Errore nel caricamento banner: {e}")
    
    def show_social_buttons(self):
        """Mostra pulsanti social"""
        social_config = self.config.get('social', {})
        discord_url = social_config.get('discord')
        simgrid_url = social_config.get('simgrid')
        
        if discord_url or simgrid_url:
            social_buttons = []
            
            if simgrid_url:
                social_buttons.append(
                    f'<a href="{simgrid_url}" target="_blank" style="text-decoration: none; margin: 0 1rem;">'
                    f'<button style="background: linear-gradient(90deg, #5865f2, #7289da); '
                    f'color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 25px; '
                    f'font-weight: bold; cursor: pointer; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">'
                    f'🏆 SimGrid Community</button></a>'
                )
            
            if discord_url:
                social_buttons.append(
                    f'<a href="{discord_url}" target="_blank" style="text-decoration: none; margin: 0 1rem;">'
                    f'<button style="background: linear-gradient(90deg, #5865f2, #7289da); '
                    f'color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 25px; '
                    f'font-weight: bold; cursor: pointer; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">'
                    f'💬 Join Discord</button></a>'
                )
            
            st.markdown(f"""
            <div style="text-align: center; margin: 1rem 0;">
                {''.join(social_buttons)}
            </div>
            """, unsafe_allow_html=True)
    
    def show_homepage(self):
        """Homepage minimale"""
        self.show_community_banner()
        
        st.markdown("---")
        
        # Metriche esempio (statiche per WIP)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-value">-</p>
                <p class="metric-label">👥 Registered Drivers</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-value">-</p>
                <p class="metric-label">🎮 Total Competitions</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-value">-</p>
                <p class="metric-label">🎉 4Fun Races</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-value">TBD</p>
                <p class="metric-label">📅 Last Session</p>
            </div>
            """, unsafe_allow_html=True)
    
    def show_work_in_progress(self):
        """Schermata Work in Progress"""
        st.markdown("""
        <div class="wip-container">
            <h1 style="font-size: 4rem; margin: 0;">🚧</h1>
            <h2 style="margin: 1rem 0;">Work in Progress</h2>
            <p style="font-size: 1.2rem; margin: 1rem 0;">
                This section is currently under development
            </p>
            <p style="font-size: 1rem; opacity: 0.9;">
                Stay tuned for updates! 🏁
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Info aggiuntive
        st.info("""
        **Coming Soon:**
        - 🏆 Championship Standings
        - 🎮 Race Results & Statistics
        - 🏁 Best Lap Times by Track
        - 👤 Driver Profiles & Stats
        - 📊 Advanced Analytics
        """)


def main():
    """Funzione principale"""
    try:
        dashboard = ACCMinimalDashboard()
        
        # Sidebar
        st.sidebar.title("🏁 Navigation")
        
        page = st.sidebar.selectbox(
            "Select page:",
            [
                "🏠 Homepage",
                "🏆 Championships",
                "🎮 4Fun Races",
                "🏁 Best Laps",
                "👤 Drivers",
                "📊 Statistics"
            ]
        )
        
        # Routing
        if page == "🏠 Homepage":
            dashboard.show_homepage()
        else:
            # Tutte le altre pagine mostrano WIP
            dashboard.show_community_banner()
            st.markdown("---")
            dashboard.show_work_in_progress()
        
        # Footer
        st.sidebar.markdown("---")
        st.sidebar.markdown(f"""
        <div style="text-align: center; color: #666; font-size: 0.8rem;">
            <p>🏁 ACC Server Dashboard</p>
            <p>Community: {dashboard.config['community']['name']}</p>
            <p>Version: 2.0 WIP</p>
        </div>
        """, unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"❌ Application Error: {e}")
        st.markdown("""
        ### 🔧 Possible Solutions:
        1. Check configuration file
        2. Reload the page
        3. Contact administrator
        """)


if __name__ == "__main__":

    main()

