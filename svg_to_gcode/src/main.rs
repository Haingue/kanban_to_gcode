use std::fs::{self};
use roxmltree::Document;
use svg2gcode::{svg2program, ConversionConfig, ConversionOptions, Machine};
use g_code::emit::{format_gcode_fmt, FormatOptions};

fn main() {
    /* Read & Parse SVG */
    let svg_path: &str = "../kanban_to_svg/resources/test.svg";
    let svg_file: String = fs::read_to_string(svg_path)
        .expect("Should have been able to read the file");
    let doc: Document<'_> = Document::parse(&svg_file)
        .expect("Should be able to parse the string as XML");

    /* Configure */
    let conf: ConversionConfig = ConversionConfig::default();
    let options: ConversionOptions = ConversionOptions {
        dimensions: [None; 2]
    };
    let machine: Machine<'_> = Machine::default();

    /* Convert to Gcode */
    let program: Vec<g_code::emit::Token<'_>> = svg2program(&doc,
        &conf,
        options,
        machine);
    let mut gcode:String = String::new();
    format_gcode_fmt(&program, FormatOptions::default(), &mut gcode)
        .expect("Should be able to convert xml(svg) to gcode");

    println!("{}", gcode)
}