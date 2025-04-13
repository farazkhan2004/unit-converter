import streamlit as st
st.title("unit_converter")

conversion_types = ["lenght","weight"]
conversion_choice = st.selectbox("chose conversion type:",conversion_types)

# lenght conversion

if conversion_choice =="lenght":
    lenght_units = ["meter","kilometer","feet","inches","centemeters"]
    input_value = st.number_input("enter lenght value:",min_value=0.0,format = "%.2f")
    from_unit = st.selectbox("from unit:",lenght_units) 
    to_unit = st.selectbox("to unit:",lenght_units)

# conversion dictionaries
    lenght_conversion = {
        "meter":1,
        "kilometer":1000,
        "feet":0.3048,
        "inches":0.0254,
        "centemeters":0.01
    }

#conversion logic
    if st.button("convert"):
        result = input_value * (lenght_conversion[from_unit] / lenght_conversion[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')


#weight conversion
elif conversion_choice =="weight":
    weight_units = ["kilograms","grams","pounds","ounces"]
    input_value = st.number_input("enter weight value:",min_value=0.0,format = "%.2f")
    from_unit = st.selectbox("from unit:",weight_units)
    to_unit = st.selectbox("to unit:",weight_units)


# conversion dictionaries

    weight_conversion = {
        "kilograms":1,
        "grams":0.001,
        "pounds":0.453592,
        "ounces":0.01
    }

#conversion logic

    if st.button("convert"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')