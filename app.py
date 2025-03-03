import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        'Length': {
            'Meter': {'Centimeter': 100, 'Kilometer': 0.001, 'Millimeter': 1000, 'Nanometer': 1e9, 'Mile': 0.000621371, 'Yard': 1.09361, 'Foot': 3.28084, 'Inch': 39.3701, 'Nautical Mile': 0.000539957},
            'Centimeter': {'Meter': 0.01, 'Kilometer': 0.00001, 'Millimeter': 10},
            'Kilometer': {'Meter': 1000, 'Centimeter': 100000},
            'Millimeter': {'Meter': 0.001, 'Centimeter': 0.1},
            'Nanometer': {'Meter': 1e-9},
            'Mile': {'Meter': 1609.34},
            'Yard': {'Meter': 0.9144},
            'Foot': {'Meter': 0.3048},
            'Inch': {'Meter': 0.0254},
            'Nautical Mile': {'Meter': 1852}
        },
        'Mass': {
            'Gram': {'Kilogram': 0.001, 'Tonne': 1e-6, 'Milligram': 1000, 'Microgram': 1e6, 'Imperial Ton': 9.8421e-7, 'US Ton': 1.1023e-6, 'Stone': 0.000157473, 'Pound': 0.00220462, 'Ounce': 0.035274},
            'Kilogram': {'Gram': 1000, 'Tonne': 0.001, 'Milligram': 1e6, 'Microgram': 1e9, 'Imperial Ton': 0.000984207, 'US Ton': 0.00110231, 'Stone': 0.157473, 'Pound': 2.20462, 'Ounce': 35.274},
            'Tonne': {'Kilogram': 1000},
            'Milligram': {'Gram': 0.001},
            'Microgram': {'Gram': 1e-6},
            'Imperial Ton': {'Kilogram': 1016.05},
            'US Ton': {'Kilogram': 907.184},
            'Stone': {'Kilogram': 6.35029},
            'Pound': {'Kilogram': 0.453592},
            'Ounce': {'Kilogram': 0.0283495}
        },
        'Time': {
            'Second': {'Minute': 1/60, 'Hour': 1/3600, 'Millisecond': 1000, 'Microsecond': 1e6, 'Nanosecond': 1e9, 'Day': 1/86400, 'Week': 1/604800, 'Month': 1/2.628e+6, 'Calendar Year': 1/3.154e+7, 'Decade': 1/3.154e+8, 'Century': 1/3.154e+9},
            'Minute': {'Second': 60, 'Hour': 1/60},
            'Hour': {'Second': 3600, 'Minute': 60},
            'Millisecond': {'Second': 0.001},
            'Microsecond': {'Second': 1e-6},
            'Nanosecond': {'Second': 1e-9},
            'Day': {'Second': 86400},
            'Week': {'Second': 604800},
            'Month': {'Second': 2.628e+6},
            'Calendar Year': {'Second': 3.154e+7},
            'Decade': {'Second': 3.154e+8},
            'Century': {'Second': 3.154e+9}
        },
        'Area': {
            'Square Kilometer': {'Square Meter': 1e6, 'Square Mile': 0.386102, 'Square Yard': 1.19599e6, 'Square Foot': 1.07639e7, 'Square Inch': 1.55e9, 'Hectare': 100, 'Acre': 247.105},
            'Square Meter': {'Square Kilometer': 1e-6, 'Square Mile': 3.861e-7, 'Square Yard': 1.19599, 'Square Foot': 10.7639, 'Square Inch': 1550, 'Hectare': 1e-4, 'Acre': 0.000247105}
        },
        'Temperature': {
            'Celsius': {'Fahrenheit': lambda x: (x * 9/5) + 32, 'Kelvin': lambda x: x + 273.15},
            'Fahrenheit': {'Celsius': lambda x: (x - 32) * 5/9, 'Kelvin': lambda x: (x - 32) * 5/9 + 273.15},
            'Kelvin': {'Celsius': lambda x: x - 273.15, 'Fahrenheit': lambda x: (x - 273.15) * 9/5 + 32}
        }
    }
    
    if from_unit == to_unit:
        return value
    
    conversion = conversion_factors.get(category, {}).get(from_unit, {}).get(to_unit)
    
    if callable(conversion):
        return conversion(value)
    
    return value * conversion if conversion else None

# Streamlit UI
st.title("Unit Converter")
st.subheader("Convert Different Units")

categories = ['Length', 'Mass', 'Time', 'Area', 'Temperature']
category = st.selectbox("Select Category", categories)

units = {
    'Length': ['Meter', 'Centimeter', 'Kilometer', 'Millimeter', 'Nanometer', 'Mile', 'Yard', 'Foot', 'Inch', 'Nautical Mile'],
    'Mass': ['Gram', 'Kilogram', 'Tonne', 'Milligram', 'Microgram', 'Imperial Ton', 'US Ton', 'Stone', 'Pound', 'Ounce'],
    'Time': ['Second', 'Minute', 'Hour', 'Millisecond', 'Microsecond', 'Nanosecond', 'Day', 'Week', 'Month', 'Calendar Year', 'Decade', 'Century'],
    'Area': ['Square Kilometer', 'Square Meter', 'Square Mile', 'Square Yard', 'Square Foot', 'Square Inch', 'Hectare', 'Acre'],
    'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin']
}

value = st.number_input("Enter Value", value=0.0)
from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("Conversion not available")
